# label

**Framework**: Evaluations  
**Kind**: property  
**Required**: Yes

A short judge-facing label for this level.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
var label: String { get }
```

#### Discussion

The default is `String(describing: self)`, which for enums produces the case name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scorelevel/label)*