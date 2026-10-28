# kABDatabaseChangedNotification

**Framework**: Address Book  
**Kind**: var  
**Role**: Global Variable

Posted when this process has changed the Address Book database.

**Availability**:
- macOS

## Declaration

```c
extern NSString * const kABDatabaseChangedNotification;
```

## Discussion

Depending on the operation performed on the address book, one or more of the following keys may be included in the user-info dictionary: `kABInsertedRecords`, `kABUpdatedRecords`, and `kABDeletedRecords`. The values for each of the keys are the unique IDs of the records that were inserted, updated, or deleted, respectively. If the values for all the keys are `nil`, every record has changes. For example, this happens when the Address Book database is restored from a backup copy.

> **Note**:  The system posts this notification on the main actor.

## See Also

### Notifications
- [kABDatabaseChangedExternallyNotification](./kabdatabasechangedexternallynotification.md)
  Posted when a process other than the current one has changed the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/kabdatabasechangednotification)*