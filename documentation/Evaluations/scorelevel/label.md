# label

**Framework**: Evaluations  
**Kind**: property  
**Required**: Yes

A short judge-facing label for this level.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
var label: String { get }
```

#### Discussion

The default is `String(describing: self)`, which for enums produces the case name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/scorelevel/label)*