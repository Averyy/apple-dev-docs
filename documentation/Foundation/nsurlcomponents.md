# NSURLComponents

**Framework**: Foundation  
**Kind**: class

An object that parses URLs into and constructs URLs from their constituent parts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSURLComponents
```

#### Overview

In Swift, this object bridges to [`URLComponents`](urlcomponents.md); use [`NSURLComponents`](nsurlcomponents.md) when you need reference semantics or other Foundation-specific behavior.

The [`NSURLComponents`](nsurlcomponents.md) class is a class that is designed to parse URLs based on [`RFC 3986`](https://developer.apple.comhttp://www.ietf.org/rfc/rfc3986.txt) and to construct URLs from their constituent parts. Its behavior differs subtly from the [`NSURL`](nsurl.md) class, which conforms to older RFCs. However, you can easily obtain an [`NSURL`](nsurl.md) object based on the contents of a URL components object or vice versa.

You create a URL components object in one of three ways: from an [`NSString`](nsstring.md) object that contains a URL, from an [`NSURL`](nsurl.md) object, or from scratch by using the default initializer. From there, you can modify the URL’s individual components and subcomponents by modifying various properties, either in unencoded form or in URL-encoded form. If you set the unencoded property, you can then obtain the encoded equivalent by reading the encoded property value and vice versa.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`URLComponents`](urlcomponents.md) structure, which bridges to the [`NSURLComponents`](nsurlcomponents.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating URL components
- [init()](nsurlcomponents/init.md)
  Creates a URL components object with all components left undefined.
- [init?(string: String)](nsurlcomponents/init(string:).md)
  Creates a URL components object by parsing a URL in string form.
- [init?(string: String, encodingInvalidCharacters: Bool)](nsurlcomponents/init(string:encodinginvalidcharacters:).md)
  Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(url: URL, resolvingAgainstBaseURL: Bool)](nsurlcomponents/init(url:resolvingagainstbaseurl:).md)
  Creates a URL components object by parsing the URL from an `NSURL` object.
### Getting the URL
- [var string: String?](nsurlcomponents/string.md)
  A URL derived from the components object, in string form.
- [var url: URL?](nsurlcomponents/url.md)
  A URL object derived from the components object.
- [func url(relativeTo: URL?) -> URL?](nsurlcomponents/url(relativeto:).md)
  Returns a URL object derived from the components object.
### Accessing components in native format
- [var fragment: String?](nsurlcomponents/fragment.md)
  The fragment URL component (the part after a `#` symbol), or nil if not present.
- [var host: String?](nsurlcomponents/host.md)
  The host URL subcomponent, or nil if not present.
- [var encodedHost: String?](nsurlcomponents/encodedhost.md)
  The host subcomponent, percent-encoded.
- [var password: String?](nsurlcomponents/password.md)
  The password URL subcomponent, or nil if not present.
- [var path: String?](nsurlcomponents/path.md)
  The path URL component, or nil if not present.
- [var port: NSNumber?](nsurlcomponents/port.md)
  The port number URL component, or nil if not present.
- [var query: String?](nsurlcomponents/query.md)
  The query URL component as a string, or nil if not present.
- [var queryItems: [URLQueryItem]?](nsurlcomponents/queryitems.md)
  The query URL component as an array of name/value pairs.
- [var scheme: String?](nsurlcomponents/scheme.md)
  The scheme URL component, or nil if not present.
- [var user: String?](nsurlcomponents/user.md)
  The username URL subcomponent, or nil if not present.
### Accessing components in URL-encoded format
- [var percentEncodedFragment: String?](nsurlcomponents/percentencodedfragment.md)
  The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedHost: String?](nsurlcomponents/percentencodedhost.md)
  The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedPassword: String?](nsurlcomponents/percentencodedpassword.md)
  The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedPath: String?](nsurlcomponents/percentencodedpath.md)
  The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedQuery: String?](nsurlcomponents/percentencodedquery.md)
  The query URL component expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedUser: String?](nsurlcomponents/percentencodeduser.md)
  The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
### Locating components in the URL string representation
- [var percentEncodedQueryItems: [URLQueryItem]?](nsurlcomponents/percentencodedqueryitems.md)
- [var rangeOfFragment: NSRange](nsurlcomponents/rangeoffragment.md)
  Returns the character range of the fragment in the string returned by the string property.
- [var rangeOfHost: NSRange](nsurlcomponents/rangeofhost.md)
  Returns the character range of the host in the string returned by the string property.
- [var rangeOfPassword: NSRange](nsurlcomponents/rangeofpassword.md)
  Returns the character range of the password in the string returned by the string property.
- [var rangeOfPath: NSRange](nsurlcomponents/rangeofpath.md)
  Returns the character range of the path in the string returned by the string property.
- [var rangeOfPort: NSRange](nsurlcomponents/rangeofport.md)
  Returns the character range of the port in the string returned by the string property.
- [var rangeOfQuery: NSRange](nsurlcomponents/rangeofquery.md)
  Returns the character range of the query in the string returned by the string property.
- [var rangeOfScheme: NSRange](nsurlcomponents/rangeofscheme.md)
  Returns the character range of the scheme in the string returned by the string property.
- [var rangeOfUser: NSRange](nsurlcomponents/rangeofuser.md)
  Returns the character range of the user in the string returned by the string property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents)*