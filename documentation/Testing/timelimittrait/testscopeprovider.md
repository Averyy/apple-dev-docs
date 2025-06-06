# TimeLimitTrait.TestScopeProvider

**Framework**: Swift Testing  
**Kind**: typealias

The type of the test scope provider for this trait.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
typealias TestScopeProvider = Never
```

#### Discussion

The default type is `Never`, which can’t be instantiated. The `scopeProvider(for:testCase:)-cjmg` method for any trait with `Never` as its test scope provider type must return `nil`, meaning that the trait doesn’t provide a custom scope for tests it’s applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/timelimittrait/testscopeprovider)*