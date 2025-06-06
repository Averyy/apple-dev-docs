# Bookmark Data Resolution Options

**Framework**: Core Foundation

Options used when resolving bookmark data.

#### Overview

When resolving a bookmark to obtain a URL, use bitwise `OR` operators to combine the options you want to specify, and provide them to the `options` parameter of the [`CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)`](cfurlcreatebyresolvingbookmarkdata(_:_:_:_:_:_:_:).md) function.

##### Version Notes

Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

## Topics

### Constants
- [static var cfBookmarkResolutionWithoutUIMask: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutuimask.md)
  Specifies that no UI feedback accompany resolution of the bookmark data.
- [static var cfBookmarkResolutionWithoutMountingMask: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutmountingmask.md)
  Specifies that no volume should be mounted during resolution of the bookmark data.
- [static var cfurlBookmarkResolutionWithSecurityScope: CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md)
  Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.

## See Also

- [Bookmark Data Creation Options](bookmark-data-creation-options.md)
  Options used when creating bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/bookmark-data-resolution-options)*