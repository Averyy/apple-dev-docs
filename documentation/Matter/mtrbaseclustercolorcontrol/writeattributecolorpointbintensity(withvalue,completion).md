# writeAttributeColorPointBIntensity(withValue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+ - Deprecated in 26.1
- iPadOS 16.4+ - Deprecated in 26.1
- Mac Catalyst 16.4+ - Deprecated in 26.1
- macOS 13.3+ - Deprecated in 26.1
- tvOS 16.4+ - Deprecated in 26.1
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 9.4+ - Deprecated in 26.1

> **Deprecated**: This attribute is no longer writable in the Matter standard

## Declaration

```swift
func writeAttributeColorPointBIntensity(withValue value: NSNumber?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAttributeColorPointBIntensity(withValue value: NSNumber?) async throws
```

```objc
- (void) writeAttributeColorPointBIntensityWithValue:(NSNumber *) value completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercolorcontrol/writeattributecolorpointbintensity(withvalue:completion:))*