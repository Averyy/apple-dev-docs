# managedObjectModel

**Framework**: AppKit  
**Kind**: property

The managed object model of the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var managedObjectModel: NSManagedObjectModel? { get }
```

#### Discussion

By default the Core Data framework creates a merged model from all models in the application bundle (`[NSBundle mainBundle]`). You can reimplement this property and return a specific model to use to create persistent stores. A typical implementation might include code similar to the following fragment:

```objc
NSBundle *bundle = [NSBundle bundleForClass:[self class]];
NSString *path = [bundle pathForResource:@"MyModel" ofType:@"mom"];
NSURL *url = [NSURL fileURLWithPath:path];
NSManagedObjectModel *model = [[NSManagedObjectModel alloc] initWithContentsOfURL:url];
```

##### Special Considerations

In applications built in OS X v10.4, by default the Core Data framework creates a merged model from all the models found in the application bundle .

## See Also

- [var managedObjectContext: NSManagedObjectContext?](nspersistentdocument/managedobjectcontext.md)
  The managed object context for the document.
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
- [func persistentStoreType(forFileType: String) -> String](nspersistentdocument/persistentstoretype(forfiletype:).md)
  Returns the type of persistent store associated with the specified file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/managedobjectmodel)*