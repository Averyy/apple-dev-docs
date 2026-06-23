# CopyMemoryDescriptor

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t CopyMemoryDescriptor(IOBufferMemoryDescriptor **mem);
```

#### Return Value

0 in case of success. Negative in case of an error.

#### Discussion

Function to get the Memory descriptor created in the Create function

## Parameters

- `mem`: The pointer to the IOBufferMemoryDescriptor object


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioextensiblepaniclog/copymemorydescriptor)*