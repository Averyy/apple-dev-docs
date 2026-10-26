# NSSharingServiceErrorMaximum

**Framework**: AppKit  
**Kind**: case  
**Role**: Enumeration Case

**Availability**:
- macOS

## Declaration

```c
NSSharingServiceErrorMaximum
```

## See Also

### Error Codes
- [NSFontAssetDownloadError](./nsfontassetdownloaderror.md)
- [NSFontErrorMaximum](./nsfonterrormaximum.md)
- [NSFontErrorMinimum](./nsfonterrorminimum.md)
- [NSTextReadInapplicableDocumentTypeError](./nstextreadinapplicabledocumenttypeerror.md)
  Indicates a problem reading data with the specified format.
- [NSTextWriteInapplicableDocumentTypeError](./nstextwriteinapplicabledocumenttypeerror.md)
  Indicates a problem writing data of the specified format.
- [NSTextReadWriteErrorMinimum](./nstextreadwriteerrorminimum.md)
  The beginning of a range of error codes reserved for future use.
- [NSTextReadWriteErrorMaximum](./nstextreadwriteerrormaximum.md)
  The end of a range of error codes reserved for future use.
- [NSServiceApplicationLaunchFailedError](./nsserviceapplicationlaunchfailederror.md)
  The service providing application could not be launched.  This will typically contain an underlying error with an Launch Services error code.
- [NSServiceApplicationNotFoundError](./nsserviceapplicationnotfounderror.md)
  The service provider could not be found.
- [NSServiceErrorMaximum](./nsserviceerrormaximum.md)
  Inclusive service error range, for checking future error codes.
- [NSServiceErrorMinimum](./nsserviceerrorminimum.md)
  Inclusive service error range, for checking future error codes.
- [NSServiceInvalidPasteboardDataError](./nsserviceinvalidpasteboarddataerror.md)
  The service providing app did not return a pasteboard with any of the promised types, or we couldn’t write the data from the pasteboard to the object receiving the returned data.
- [NSServiceMalformedServiceDictionaryError](./nsservicemalformedservicedictionaryerror.md)
  The service dictionary did not contain the necessary keys.  Messages will typically be logged to the console giving more details.
- [NSServiceMiscellaneousError](./nsservicemiscellaneouserror.md)
  Other errors, representing programmatic mistakes in the service consuming application.  These show a generic error message to the user.
- [NSServiceRequestTimedOutError](./nsservicerequesttimedouterror.md)
  The service providing application did not open its service listening port in time, or the app didn’t respond to the request in time; see the Console log to figure out which (the errors are typically reported the same way to the user).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingserviceerrormaximum)*