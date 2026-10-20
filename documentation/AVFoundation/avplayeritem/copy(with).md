# copy(with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a copy of the object with the specified zone.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func copy(with zone: NSZone? = nil) -> Any
```

```objc
- (id) copyWithZone:(NSZone *) zone;
```

#### Return Value

A copy of the original asset instance.

## Parameters

- `zone`: The system ignores this parameter.

## See Also

### Copying an player item
- [func copy() -> Any](./copy%28%29.md)
  Creates a copy of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/copy(with:))*