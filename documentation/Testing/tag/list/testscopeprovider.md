# Tag.List.TestScopeProvider

**Framework**: Swift Testing  
**Kind**: typealias

The type of the test scope provider for this trait.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
typealias TestScopeProvider = Never
```

#### Discussion

The default type is `Never`, which can’t be instantiated. The `scopeProvider(for:testCase:)-cjmg` method for any trait with `Never` as its test scope provider type must return `nil`, meaning that the trait doesn’t provide a custom scope for tests it’s applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/tag/list/testscopeprovider)*