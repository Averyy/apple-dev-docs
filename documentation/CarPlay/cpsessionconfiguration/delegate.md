# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The custom object you use to handle changes to environment values.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var delegate: (any CPSessionConfigurationDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<CPSessionConfigurationDelegate> delegate;
```

## Discussion

This property stores the object you provide at initialization time, but you can change it later if needed. When environment values change, the [`CPSessionConfiguration`](../cpsessionconfiguration.md) object responds by calling the methods of the object in this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration/delegate)*