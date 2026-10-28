# Enabling AutoFill for domain-bound SMS codes

**Framework**: Security  
**Role**: Article

Streamline entering codes you send as SMS messages.

## Overview

Some internet services that authenticate people with passwords send verification codes using SMS. The service sends a random one-time code to the phone number that the person added to their account profile. The person enters the code into the website or app as additional evidence that they’re accessing their own account.

In iOS 14 or later and macOS Big Sur or later, format the SMS messages you send to bind your service’s one-time codes with its DNS domain. AutoFill only suggests a domain-bound code to a person when the website they’re browsing in Safari, or an associated domain for the app they’re using, matches the domain in the SMS code. This makes it harder for an attacker to trick someone into entering one-time codes into a phishing website.

### Configure your app’s associated domains

AutoFill suggests domain-bound codes in your app if the bound domain in the message is one of the app’s associated domains. For information on configuring associated domains, see [Supporting associated domains](../Xcode/supporting-associated-domains.md).

### Set your one-time code text field’s content type

For UIKit apps on iOS and Mac Catalyst, set your one-time code field’s [`textContentType`](../UIKit/uitextinputtraits/textcontenttype.md) property to [`oneTimeCode`](../UIKit/uitextcontenttype/onetimecode.md). For AppKit apps on macOS, set your one-time code field’s [`contentType`](../AppKit/nstextcontent/contenttype.md) property to [`oneTimeCode`](../AppKit/nstextcontenttype/onetimecode.md). For SwiftUI apps, use the [`textContentType(_:)`](../SwiftUI/view/textcontenttype%28_%29-ufdv.md) view modifier to set the content type to [`oneTimeCode`](../UIKit/uitextcontenttype/onetimecode.md).

For your website, set the HTML `<input>` element attribute `autocomplete=one-time-code`.

### Format your SMS messages

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