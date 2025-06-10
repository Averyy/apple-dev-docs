# init(_:reason:context:result:)

**Framework**: Local Authentication  
**Kind**: init

Creates a new `LocalAuthenticationView`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ title: LocalizedStringResource, reason: Text, context: LAContext? = nil, result: @escaping (Result<Void, any Error>) -> Void) where Label == Text
```

#### Discussion

The view takes `LAContext` instance or creates own one if none provided and starts evaluating `deviceOwnerAuthenticationWithBiometricsOrCompanion` policy. The result of authentication is reported back using `result` closure.

## Parameters

- `title`: Title shown below the authentication view.
- `reason`: Localized reason used for policy evaluation.
- `context`:   instance used for policy evaluation.
- `result`: Result closure used for reporting the result of authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(_:reason:context:result:)-88u6u)*