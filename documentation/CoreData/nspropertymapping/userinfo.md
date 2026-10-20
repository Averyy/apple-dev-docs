# userInfo

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The user info for the property mapping.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

```objc
@property (strong, nullable) NSDictionary * userInfo;
```

## See Also

### Managing Mapping Attributes
- [var name: String?](./name.md)
  The name of the property in the destination entity for the property mapping.
- [var valueExpression: NSExpression?](./valueexpression.md)
  The value expression for the property mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertymapping/userinfo)*