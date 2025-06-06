# Enabling AutoFill for domain-bound SMS codes

**Framework**: Security

Streamline entering codes you send as SMS messages.

#### Overview

Some internet services that authenticate people with passwords send verification codes using SMS. The service sends a random one-time code to the phone number that the person added to their account profile. The person enters the code into the website or app as additional evidence that they’re accessing their own account.

In iOS 14 or later and macOS Big Sur or later, format the SMS messages you send to bind your service’s one-time codes with its DNS domain. AutoFill only suggests a domain-bound code to a person when the website they’re browsing in Safari, or an associated domain for the app they’re using, matches the domain in the SMS code. This makes it harder for an attacker to trick someone into entering one-time codes into a phishing website.

##### Configure Your Apps Associated Domains

AutoFill suggests domain-bound codes in your app if the bound domain in the message is one of the app’s associated domains. For information on configuring associated domains, see [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains).

##### Set Your One Time Code Text Fields Content Type

For UIKit apps on iOS and Mac Catalyst, set your one-time code field’s [`textContentType`](https://developer.apple.com/documentation/UIKit/UITextInputTraits/textContentType) property to [`oneTimeCode`](https://developer.apple.com/documentation/UIKit/UITextContentType/oneTimeCode). For AppKit apps on macOS, set your one-time code field’s [`contentType`](https://developer.apple.com/documentation/AppKit/NSTextContent/contentType) property to [`oneTimeCode`](https://developer.apple.com/documentation/AppKit/NSTextContentType/oneTimeCode). For SwiftUI apps, use the [`textContentType(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)-ufdv) view modifier to set the content type to [`oneTimeCode`](https://developer.apple.com/documentation/UIKit/UITextContentType/oneTimeCode).

For your website, set the HTML `<input>` element attribute `autocomplete=one-time-code`.

##### Format Your Sms Messages

You can present any information at the start of the SMS message, in any format. The last line of your message needs your DNS domain name, prefixed by an at sign (`@`), and the one-time code, prefixed by a hash symbol (`#`). Separate the two components using a space. For example:

```console
Your Example code is 123456.

@example.com #123456
```

If your website embeds its login view in an iFrame, which uses a different DNS domain than the main website, additionally include the DNS domain name for the embedded login view, prefixed by the percent sign (`%`). For example:

```console
Your Example code is 123456.

@example.com #123456 %iframe-auth.example.org
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/enabling-autofill-for-domain-bound-sms-codes)*