# initWithIdentifier:name:

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Create a new configuration with an identifier and a name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier name:(NSString *) name;
```

## Parameters

- `identifier`: A string that uniquely identifies the tool in the picker, such as `com.example.example-company.custom-tool`.
- `name`: A short string to show as the name of the tool in the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitemconfiguration/initwithidentifier:name:)*