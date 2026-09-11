# reduce(into:value:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Reduces a property value into an accumulating summary.

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
static func reduce(into summary: inout Self.Summary, value: Self.Value)
```

#### Discussion

This method is called to incorporate individual property values into a summary that represents the aggregated state across multiple progress managers.

## Parameters

- `summary`: The accumulating summary value to modify.
- `value`: The individual property value to incorporate into the summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/property/reduce(into:value:))*