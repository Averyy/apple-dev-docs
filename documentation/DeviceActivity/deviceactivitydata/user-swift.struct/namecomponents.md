# nameComponents

**Framework**: Device Activity  
**Kind**: property  
**Role**: Instance Property

Access the name of the person.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var nameComponents: PersonNameComponents?
```

#### Discussion

You can use this property to construct the person’s name for display. Use the components with an instance of [`PersonNameComponentsFormatter`](../../../Foundation/personnamecomponentsformatter.md) to create a string representation for the current locale.

## See Also

### Identifying the person
- [var appleID: String?](./appleid.md)
  Access the Apple ID of the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/user-swift.struct/namecomponents)*