# configurationDescriptor(withConfigurationValue:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func configurationDescriptor(withConfigurationValue configurationValue: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>
```

```objc
- (const IOUSBConfigurationDescriptor *) configurationDescriptorWithConfigurationValue:(NSUInteger) configurationValue error:(NSError **) error;
```

## See Also

### Instance Methods
- [func configurationDescriptor(with: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>](./configurationdescriptor%28with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/configurationdescriptor(withconfigurationvalue:))*