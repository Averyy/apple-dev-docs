# configurationWithConfiguration:

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Type Method

Convenience method for getting a CWConfiguration object initialized with the given CWConfiguration object.

**Availability**:
- macOS 10.7+

## Declaration

```objc
+ (instancetype) configurationWithConfiguration:(CWConfiguration *) configuration;
```

## Return Value

A CWConfiguration object.

## Parameters

- `configuration`: The CWConfiguration object to use to initialize a new CWConfiguration object.

## See Also

### Creating a configuration
- [init()](./init%28%29.md)
  Creates an empty CWConfiguration object.
- [init(configuration: CWConfiguration)](./init%28configuration%29.md)
  Creates and returns a CWConfiguration object initialized with the given CWConfiguration object.
- [+ configuration](./configuration.md)
  Convenience method for getting an empty CWConfiguration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwconfiguration/configurationwithconfiguration:)*