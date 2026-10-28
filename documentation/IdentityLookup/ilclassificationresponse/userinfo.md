# userInfo

**Framework**: SMS and Call Reporting  
**Kind**: property  
**Role**: Instance Property

JSON data included in a response sent over the network.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var userInfo: [String : Any]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSDictionary<NSString *,id> * userInfo;
```

## Discussion

Use this property if you set the `ILClassificationExtensionNetworkReportDestination` key in the extension’s `Info.plist` file. The property stores any additional data that you want to pass to your servers as part of the response. Both the keys and values must be JSON-serializable. For more information, see [`JSONSerialization`](../../Foundation/jsonserialization.md).

## See Also

### Accessing Data
- [var action: ILClassificationAction](./action.md)
  A classification that determines what action the system takes.
- [var userString: String?](./userstring.md)
  Text included in a response sent over SMS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationresponse/userinfo)*