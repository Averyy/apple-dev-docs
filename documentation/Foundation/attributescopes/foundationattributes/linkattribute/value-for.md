# value(for:)

**Framework**: Foundation  
**Kind**: method

Returns the URL value of the specified object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func value(for object: NSObject) throws -> URL
```

#### Return Value

A URL value.

## Parameters

- `object`: An [`NSObject`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class) to retrieve a URL value from.

## See Also

- [static var name: String](attributescopes/foundationattributes/linkattribute/name.md)
  The name of the link attribute.
- [AttributeScopes.FoundationAttributes.LinkAttribute.Value](attributescopes/foundationattributes/linkattribute/value.md)
  The type of the link attribute’s value.
- [static func objectiveCValue(for: URL) throws -> NSObject](attributescopes/foundationattributes/linkattribute/objectivecvalue(for:).md)
  Returns an object for a specified URL value.
- [AttributeScopes.FoundationAttributes.LinkAttribute.ObjectiveCValue](attributescopes/foundationattributes/linkattribute/objectivecvalue.md)
  The type of the link attribute’s value when calling it from Objective-C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/linkattribute/value(for:))*