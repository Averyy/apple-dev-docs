# requiresUserAccountType

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

Specifies the type of user account required to start an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var requiresUserAccountType: AEUserAccountType { get set }
```

```objc
@property (nonatomic, assign) AEUserAccountType requiresUserAccountType;
```

#### Discussion

This property defines the account requirement for starting an assessment session. Set it to `.standard` to require a non-administrator account, `.guest` to require a guest account, or `.any` (the default) to allow any account type.

> **See Also**: [`AEUserAccountType`](../aeuseraccounttype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/requiresuseraccounttype)*