# stringEdited(in:changeInLength:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the linguistic tagger that the string (if mutable) has changed as specified by the parameters.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.7+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
func stringEdited(in newRange: NSRange, changeInLength delta: Int)
```

```objc
- (void) stringEditedInRange:(NSRange) newRange changeInLength:(NSInteger) delta;
```

## Parameters

- `newRange`: The range in the final string that was edited.
- `delta`: The change in length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/stringedited(in:changeinlength:))*