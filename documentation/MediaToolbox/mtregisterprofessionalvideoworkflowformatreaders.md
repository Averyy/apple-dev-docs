# MTRegisterProfessionalVideoWorkflowFormatReaders()

**Framework**: Mediatoolbox  
**Kind**: func

Enables the use of media format readers that support professional video workflows.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func MTRegisterProfessionalVideoWorkflowFormatReaders()
```

#### Overview

Call this function to indicate to Media Toolbox that your app requires support for [`MediaExtension`](https://developer.apple.com/documentation/MediaExtension) format readers.

> **Note**: This functionality is only intended for apps that support professional video workflows. It isn’t recommended for network-facing applications such as web browsers, messaging clients, mail clients, and so on.

By convention, format readers registered using this function should conform to the abstract [`UTTypeReference`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeReference) of `com.apple.mediaextension-content` which in turn conforms to the abstract type `public.movie`. You can use `com.apple.mediaextension-content` to do type filtering (for example in Open… dialogs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtregisterprofessionalvideoworkflowformatreaders())*