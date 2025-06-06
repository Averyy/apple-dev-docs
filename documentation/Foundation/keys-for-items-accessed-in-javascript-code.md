# Keys for Items Accessed in JavaScript Code

**Framework**: Foundation

Keys in property list items that the system recieves from or sends to JavaScript code.

## Topics

### Constants
- [let NSExtensionJavaScriptPreprocessingResultsKey: String](nsextensionjavascriptpreprocessingresultskey.md)
  A key whose value is an item of type `kUTTypePropertyList`. The item contains an `NSDictionary` that contains the object returned by the JavaScript code to its completion function.
- [let NSExtensionJavaScriptFinalizeArgumentKey: String](nsextensionjavascriptfinalizeargumentkey.md)
  A key whose value is an item of type `kUTTypePropertyList`. The item contains an `NSDictionary` that contains the arguments to be passed to a JavaScript finalize method.

## See Also

- [NSItemProvider.CompletionHandler](nsitemprovider/completionhandler.md)
  A block that receives the item provider’s data.
- [NSItemProvider.LoadHandler](nsitemprovider/loadhandler.md)
  A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md)
  Keys indicating options to use when generating the item provider’s data.
- [class let errorDomain: String](nsitemprovider/errordomain.md)
  The error domain associated with the item provider.
- [struct NSItemProviderFileOptions](nsitemproviderfileoptions.md)
  Data-access specifications that declare how to handle items.
- [protocol NSItemProviderReading](nsitemproviderreading.md)
  The protocol for implementing a class to allow an item provider to create an instance of the class.
- [protocol NSItemProviderWriting](nsitemproviderwriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [enum NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md)
  Specifications that control which categories of processes can see an item.
- [NSItemProvider.ErrorCode](nsitemprovider/errorcode.md)
  The error codes that describe problems with consuming data from an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/keys-for-items-accessed-in-javascript-code)*