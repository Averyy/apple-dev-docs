# parent

**Framework**: Swift Testing  
**Kind**: property

The ID of the parent test.

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
var parent: Test.ID? { get }
```

#### Discussion

If this test’s ID has no parent (i.e. the test is at the root of a test graph), the value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test/id-swift.struct/parent)*