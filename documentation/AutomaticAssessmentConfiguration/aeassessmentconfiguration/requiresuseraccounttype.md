# requiresUserAccountType

**Framework**: Automatic Assessment Configuration  
**Kind**: property

Specifies the type of user account required to start an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var requiresUserAccountType: AEUserAccountType { get set }
```

#### Discussion

This property defines the account requirement for starting an assessment session. Set it to `.standard` to require a non-administrator account, `.guest` to require a guest account, or `.any` (the default) to allow any account type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiresuseraccounttype)*