# profileNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The profile index from which to restore the settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * profileNumber;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * profileNumber;
```

#### Discussion

If your vehicle saves profile information using defined indexes, use this property to get the integer index of the profile slot from which to retrieve the settings.

## See Also

### Getting the Profile Information
- [defaultProfile](./defaultprofile-4ztep.md)
  A Boolean value indicating whether to make the profile the default profile.
- [var profileName: String?](./profilename.md)
  The name assigned to the profile.
- [var profileLabel: String?](./profilelabel.md)
  The name assigned to the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent/profilenumber-50f30)*