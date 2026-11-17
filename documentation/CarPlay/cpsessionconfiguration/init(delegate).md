# init(delegate:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Configures a session configuration with the custom delegate object you provide.

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

## Return Value

A new session configuration object with the specified delegate.

## Parameters

- `delegate`: A custom type you use to handle subsequent changes to environment values.

## See Also

### Creating a session configuration
- [protocol CPSessionConfigurationDelegate](../cpsessionconfigurationdelegate.md)
  Methods you use to respond to changes in the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration/init(delegate:))*