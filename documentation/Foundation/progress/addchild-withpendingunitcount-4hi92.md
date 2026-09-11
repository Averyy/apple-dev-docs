# addChild(_:withPendingUnitCount:)

**Framework**: Foundation  
**Kind**: method

Adds a ProgressReporter as a child to a Progress, which constitutes a portion of Progress’s totalUnitCount.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func addChild(_ reporter: ProgressReporter, withPendingUnitCount count: Int)
```

## Parameters

- `reporter`: A `ProgressReporter` instance.
- `count`: Number of units delegated from `self`’s `totalCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/addchild(_:withpendingunitcount:)-4hi92)*