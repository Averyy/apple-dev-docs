# init(rawValue:)

**Framework**: Core ML  
**Kind**: init

Creates a progress event for the given integer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(rawValue: Int)
```

#### Discussion

You do not use this initializer directly. Get update event types from the type properties, such as [`trainingBegin`](mlupdateprogressevent/trainingbegin.md), [`miniBatchEnd`](mlupdateprogressevent/minibatchend.md), or [`epochEnd`](mlupdateprogressevent/epochend.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdateprogressevent/init(rawvalue:))*