# supportedFamilies

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The families that support this type of complication.

**Availability**:
- watchOS 7.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * supportedFamilies;
```

## Discussion

Different descriptors can support different sets of families.

## See Also

### Accessing the descriptor’s data
- [var identifier: String](./identifier.md)
  A string that uniquely identifies the descriptor.
- [var displayName: String](./displayname.md)
  A localized string that identifies complications from the descriptor to the user.
- [var userActivity: NSUserActivity?](./useractivity.md)
  A user activity object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  A dictionary of data that your data source can use to generate timeline entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor/supportedfamilies-50ink)*