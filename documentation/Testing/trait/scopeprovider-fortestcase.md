# scopeProvider(for:testCase:)

**Framework**: Swift Testing  
**Kind**: method  
**Required**: Yes

Get this trait’s scope provider for the specified test and optional test case.

**Availability**:
- Swift 6.1+
- Xcode 16.3+

## Declaration

```swift
func scopeProvider(for test: Test, testCase: Test.Case?) -> Self.TestScopeProvider?
```

#### Return Value

A value conforming to [`TestScopeProvider`](trait/testscopeprovider.md) which you use to provide custom scoping for `test` or `testCase`. Returns `nil` if the trait doesn’t provide any custom scope for the test or test case.

#### Discussion

If this trait’s type conforms to [`TestScoping`](testscoping.md), the default value returned by this method depends on the values of`test` and `testCase`:

- If `test` represents a suite, this trait must conform to [`SuiteTrait`](suitetrait.md). If the value of this suite trait’s [`isRecursive`](suitetrait/isrecursive.md) property is `true`, then this method returns `nil`, and the suite trait provides its custom scope once for each test function the test suite contains. If the value of [`isRecursive`](suitetrait/isrecursive.md) is `false`, this method returns `self`, and the suite trait provides its custom scope once for the entire test suite.
- If `test` represents a test function, this trait also conforms to [`TestTrait`](testtrait.md). If `testCase` is `nil`, this method returns `nil`; otherwise, it returns `self`. This means that by default, a trait which is applied to or inherited by a test function provides its custom scope once for each of that function’s cases.

A trait may override this method to further customize the default behaviors above. For example, if a trait needs to provide custom test scope both once per-suite and once per-test function in that suite, it implements the method to return a non-`nil` scope provider under those conditions.

A trait may also implement this method and return `nil` if it determines that it does not need to provide a custom scope for a particular test at runtime, even if the test has the trait applied. This can improve performance and make diagnostics clearer by avoiding an unnecessary call to [`provideScope(for:testCase:performing:)`](testscoping/providescope(for:testcase:performing:).md).

If this trait’s type does not conform to [`TestScoping`](testscoping.md) and its associated [`TestScopeProvider`](trait/testscopeprovider.md) type is the default `Never`, then this method returns `nil` by default. This means that instances of this trait don’t provide a custom scope for tests to which they’re applied.

## Parameters

- `test`: The test for which a scope provider is being requested.
- `testCase`: The test case for which a scope provider is being requested,   if any. When   represents a suite, the value of this argument is   .

## See Also

- [protocol TestScoping](testscoping.md)
  A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.
- [associatedtype TestScopeProvider : TestScoping = Never](trait/testscopeprovider.md)
  The type of the test scope provider for this trait.
- [func prepare(for: Test) async throws](trait/prepare(for:).md)
  Prepare to run the test that has this trait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/scopeprovider(for:testcase:))*