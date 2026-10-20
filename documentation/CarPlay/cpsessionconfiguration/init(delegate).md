# init(delegate:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a session configuration with a delegate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(delegate: any CPSessionConfigurationDelegate)
```

```objc
- (instancetype) initWithDelegate:(id<CPSessionConfigurationDelegate>) delegate;
```

#### Return Value

A newly initialized session configuration.

## Parameters

- `delegate`: The delegate object.

## See Also

### Creating a Session Configuration
- [protocol CPSessionConfigurationDelegate](../cpsessionconfigurationdelegate.md)
  A protocol for receiving notifications about changes to vehicle properties and configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration/init(delegate:))*