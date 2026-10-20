# init(coder:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a location sort descriptor from a serialized instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Parameters

- `aDecoder`: The coder to use when deserializing the location sort descriptor.

## See Also

### Creating a Location Sort Descriptor
- [init(key: String, relativeLocation: CLLocation)](./init%28key,relativelocation%29.md)
  Creates a location sort descriptor using the specified key and relative location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/init(coder:))*