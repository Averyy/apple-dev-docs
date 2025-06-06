# companions

**Framework**: Local Authentication  
**Kind**: property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var companions: [LAEnvironment.MechanismCompanion] { get }
```

#### Discussion

```None
        this property enumerates paired companions, even if they are not reachable at the moment. Check @c isUsable
        property to determine if a particular companion type is available for use. 
        Note that items in this array represent paired companion types, not individual devices. Therefore, even if the user
        has paired multiple Apple Watch devices for companion authentication, the array will contain only one
        @c LAEnvironmentMechanimsCompanion instance of type @c LACompanionTypeWatch.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/state-swift.class/companions)*