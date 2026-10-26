---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkitem"
framework: "CareKit/CareKitUI"
---

# LinkItem

**Framework**: CareKit/CareKitUI  
**Kind**: enum  
**Role**: Enumeration

A link item tied to a button in the `LinkView`.

## Declaration

```swift
enum LinkItem
```

## Topics

### Enumeration Cases
- [case appStore(id: String, title: String)](./linkitem/appstore%28id,title%29.md)
  Link to open an app in the App Store.
- [case call(phoneNumber: String, title: String)](./linkitem/call%28phonenumber,title%29.md)
  Link to call a phone number.
- [case email(recipient: String, title: String)](./linkitem/email%28recipient,title%29.md)
  Link to email a recipient.
- [case location(String, String, title: String)](./linkitem/location%28_,_,title%29.md)
  Link to a location in Maps.
- [case message(phoneNumber: String, title: String)](./linkitem/message%28phonenumber,title%29.md)
  Link to message a phone number.
- [case url(URL, title: String, symbol: String)](./linkitem/url%28_,title,symbol%29.md)
  Link to a generic URL.
- [case website(String, title: String)](./linkitem/website%28_,title%29.md)
  Link to a website. Supports opening in app.
### Instance Properties
- [var url: URL?](./linkitem/url.md)
  The URL for the current link.
### Default Implementations
- [Equatable Implementations](./linkitem/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable

## See Also

### Links
- [struct LinkView](./linkview.md)
  A card that displays multiple link buttons. Links buttons are capable of showing content in or out of app. Link buttons can be configured using a `Link`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkitem)*