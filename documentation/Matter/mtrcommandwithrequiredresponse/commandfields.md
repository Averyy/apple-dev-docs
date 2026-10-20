# commandFields

**Framework**: Matter  
**Kind**: property  
**Role**: Instance Property

The command fields to pass for the command invoke.  nil if this command does not have any fields.  If not nil, this should be a data-value dictionary of MTRStructureValueType.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
var commandFields: [String : Any]? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSDictionary<NSString *,id> * commandFields;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommandwithrequiredresponse/commandfields)*