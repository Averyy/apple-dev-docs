# ABAddressBookRequestAccessCompletionHandler

**Framework**: Address Book  
**Kind**: typealias

Definition for a block callback invoked when an access request has completed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
typealias ABAddressBookRequestAccessCompletionHandler = (Bool, CFError?) -> Void
```

#### Discussion

Address book request access completion handler blocks are used with [`ABAddressBookCreateWithOptions(_:_:)`](abaddressbookcreatewithoptions(_:_:).md). If you had a view controller that wanted to display the count of users with the name “Smith” in the address book, you might implement something like the code shown in the following code listing.

Listing 1. Sample implementation using ABAddressBookRequestAccessCompletionHandler

```objc
@implementation APLViewController
 
- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view
    CFErrorRef myError = NULL;
    ABAddressBookRef myAddressBook = ABAddressBookCreateWithOptions(NULL, &myError);
    APLViewController * __weak weakSelf = self;  // avoid capturing self in the block
    ABAddressBookRequestAccessWithCompletion(myAddressBook,
      ^(bool granted, CFErrorRef error) {
        if (granted) {
            NSArray *theSmiths = CFBridgingRelease(
              ABAddressBookCopyPeopleWithName(myAddressBook,
                CFSTR("Smith")
              )
            );
            weakSelf.numberOfSmiths = [theSmiths count];
        } else {
            // Handle the case of being denied access and/or the error.
        }
        CFRelease(myAddressBook);
    });
}
 
...
 
@end
```

## See Also

- [typealias ABExternalChangeCallback](abexternalchangecallback.md)
  Prototype for a function callback invoked on an address book when the Address Book database is modified by another address book instance.
- [typealias ABMultiValueIdentifier](abmultivalueidentifier.md)
  Identifies multivalue properties.
- [typealias ABPersonCompositeNameFormat](abpersoncompositenameformat.md)
  Indicates a person-name display format.
- [typealias ABPersonSortOrdering](abpersonsortordering.md)
  Indicates a person sort ordering.
- [typealias ABPropertyID](abpropertyid.md)
  Integer that identifies a record property.
- [typealias ABRecordID](abrecordid.md)
  Integer that identifies a record.
- [typealias ABRecordType](abrecordtype.md)
  Integer that identifies a record type.
- [typealias ABSourceType](absourcetype.md)
  Indicates a source type. See `Source Properties`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbookrequestaccesscompletionhandler)*