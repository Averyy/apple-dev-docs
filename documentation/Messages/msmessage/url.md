# url

**Framework**: Messages  
**Kind**: property

A URL that encodes data to be transmitted with the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var url: URL? { get set }
```

#### Discussion

Encode your application’s data in the URL. For example, you can encode data as key-value pairs in the URL’s query string, as shown below:

```swift
guard let components = NSURLComponents(string: myBaseURL) else {
    fatalError("Invalid base url")
}
 
let size = NSURLQueryItem(name: "Size", value: "Large")
let count = NSURLQueryItem(name: "Topping_Count", value: "2")
let cheese = NSURLQueryItem(name: "Topping_0", value: "Cheese")
let pepperoni = NSURLQueryItem(name: "Topping_1", value: "Pepperoni")
components.queryItems = [size, count, cheese, pepperoni]
 
guard let url = components.url  else {
    fatalError("Invalid URL components.")
}
 
message.url = url
```

The message object is delivered to the extension running on the recipient’s device. The extension can access the session’s current state from the message’s `URL` property, as shown below:

```swift
guard let components = NSURLComponents(url: message.url, resolvingAgainstBaseURL: false) else {
    fatalError("The message contains an invalid URL")
}
 
if let queryItems = components.queryItems {
    // process the query items here...
}
```

If the message is selected on macOS, the system loads the URL in a web browser. The URL should point to a web service that returns a meaningful result based on the encoded data.

The URL property must use an HTTP, HTTPS, or data scheme. Custom app schemes are not supported. Additionally, the URL cannot be longer than 5,000 characters.

By default, this property is set to `nil`.

## See Also

- [var accessibilityLabel: String?](msmessage/accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](msmessage/error.md)
  An error object describing why the system failed to send the message.
- [var isPending: Bool](msmessage/ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](msmessage/layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](msmessage/senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](msmessage/session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](msmessage/shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](msmessage/summarytext.md)
  A succinct description of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/url)*