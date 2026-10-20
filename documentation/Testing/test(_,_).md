# Test(_:_:)

**Framework**: Swift Testing  
**Kind**: macro  
**Role**: Macro

Declare a test.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
@attached
(peer) macro Test(_ displayName: String? = nil, _ traits: any TestTrait...)
```

## Parameters

- `displayName`: The customized display name of this test. If the value of this argument is `nil`, the display name of the test is derived from the associated function’s name.
- `traits`: Zero or more traits to apply to this test.

## See Also

### Related Documentation
- [Defining test functions](./definingtests.md)
  Define a test function to validate that code is working correctly.
### Essentials
- [Defining test functions](./definingtests.md)
  Define a test function to validate that code is working correctly.
- [Organizing test functions with suite types](./organizingtests.md)
  Organize tests into test suites.
- [Migrating a test from XCTest](./migratingfromxctest.md)
  Migrate an existing test method or test class written using XCTest.
- [struct Test](./test.md)
  A type representing a test or suite.
- [macro Suite(String?, any SuiteTrait...)](./suite%28_,_%29.md)
  Declare a test suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test(_:_:))*