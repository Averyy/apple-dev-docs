# accessibilityElement(children:)

**Framework**: App Intents  
**Kind**: method

Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibilityElement(children: AccessibilityChildBehavior = .ignore) -> some View
```

#### Discussion

See also:

- `AccessibilityChildBehavior/ignore`
- `AccessibilityChildBehavior/combine`
- `AccessibilityChildBehavior/contain`

## Parameters

- `children`: The behavior to use when creating or   transforming an accessibility element.   The default is 


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilityelement(children:))*