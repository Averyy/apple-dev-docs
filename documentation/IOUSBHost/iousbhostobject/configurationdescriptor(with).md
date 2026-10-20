# configurationDescriptor(with:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func configurationDescriptor(with index: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>
```

```objc
- (const IOUSBConfigurationDescriptor *) configurationDescriptorWithIndex:(NSUInteger) index error:(NSError **) error;
```

## See Also

### Instance Methods
- [func configurationDescriptor(withConfigurationValue: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>](./configurationdescriptor%28withconfigurationvalue%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/configurationdescriptor(with:))*