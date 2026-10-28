# identifier

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

A string that uniquely identifies the tool in the picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```objc
@property (nonatomic, copy) NSString * identifier;
```

## Discussion

For example, you might use the name `com.example.example-company.custom-tool`. If you use multiple tool items with the same identifier to create the picker, the picker only shows the first instance of that item.

## See Also

### Identifying the custom item
- [name](./name.md)
  A short string to show as the name of the tool in the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitemconfiguration/identifier)*