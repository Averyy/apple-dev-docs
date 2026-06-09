# subprogress(assigningCount:)

**Framework**: Foundation  
**Kind**: method

Returns a Subprogress which can be passed to any method that reports progress It can be then used to create a child `ProgressManager` reporting to this `Progress`

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func subprogress(assigningCount count: Int) -> Subprogress
```

#### Return Value

A `Subprogress` instance.

#### Discussion

Delegates a portion of totalUnitCount to a future child `ProgressManager` instance.

## Parameters

- `count`: Number of units delegated to a child instance of `ProgressManager` which may be instantiated by `Subprogress` later when `reporter(totalCount:)` is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/subprogress(assigningcount:))*