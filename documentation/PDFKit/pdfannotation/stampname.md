# stampName

**Framework**: PDFKit  
**Kind**: property

The name of the stamp, a text or graphics annotation that emulates a rubber stamp effect.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var stampName: String? { get set }
```

#### Discussion

The default value for this property is `Default`. Additional possible values for `stampName` are: `Approved`, `Asis`, `Confidential`, `Departmental`, `Experimental`, `Expired`, `Final`, `ForComment`, `ForPublicRelease`, `NotApproved`, `NotForPublicRelease`, `Sold`, and `TopSecret`. Custom values are also supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/stampname)*