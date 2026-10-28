# objectiveCValue(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an object for a specified URL value.

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
static func objectiveCValue(for value: URL) throws -> NSObject
```

## Return Value

The object for the specified URL.

## Parameters

- `value`: A URL to produce an [`NSObject`](../../../../ObjectiveC/nsobject-swift.class.md) from.

## See Also

### Accessing the Attribute Name and Value
- [static var name: String](./name.md)
  The name of the link attribute.
- [static func value(for: NSObject) throws -> URL](./value%28for%29.md)
  Returns the URL value of the specified object.
- [AttributeScopes.FoundationAttributes.LinkAttribute.Value](./value.md)
  The type of the link attribute’s value.
- [AttributeScopes.FoundationAttributes.LinkAttribute.ObjectiveCValue](./objectivecvalue.md)
  The type of the link attribute’s value when calling it from Objective-C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/linkattribute/objectivecvalue(for:))*