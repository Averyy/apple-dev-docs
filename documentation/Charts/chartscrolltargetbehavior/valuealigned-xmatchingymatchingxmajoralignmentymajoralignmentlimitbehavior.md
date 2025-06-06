# valueAligned(xMatching:yMatching:xMajorAlignment:yMajorAlignment:limitBehavior:)

**Framework**: Swift Charts  
**Kind**: method

Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func valueAligned(xMatching xComponents: DateComponents, yMatching yComponents: DateComponents, xMajorAlignment: MajorValueAlignment<Date>? = nil, yMajorAlignment: MajorValueAlignment<Date>? = nil, limitBehavior: ValueAlignedLimitBehavior = .automatic) -> ValueAlignedChartScrollTargetBehavior where Self == ValueAlignedChartScrollTargetBehavior
```

## Parameters

- `xComponents`: The alignment components for the x-axis.
- `yComponents`: The alignment components for the y-axis.
- `xMajorAlignment`: The behavior for aligning to major values along the x-axis.
- `yMajorAlignment`: The behavior for aligning to major values along the y-axis.
- `limitBehavior`: The scroll limit behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartscrolltargetbehavior/valuealigned(xmatching:ymatching:xmajoralignment:ymajoralignment:limitbehavior:))*