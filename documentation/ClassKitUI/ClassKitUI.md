# ClassKit UI

**Framework**: ClassKit UI  
**Kind**: module

Display views that enable students to submit and withdraw assigned documents in your app.

#### Overview

ClassKit UI helps students manage their assigned documents within your app. When teachers assign activities, students use these views to perform actions such as submit their work, withdraw submissions, and track their progress within your app.

The framework provides views for both submitting assigned documents and displaying submission information like status and due dates. Each view automatically fetches assigned document data from ClassKit and updates when the submission status changes. You can customize the submission process with [`closures`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/) that execute before and after submissions. For example, when a student tries to submit a document for an assignment, your app can verify that the document is ready to submit. And after submitting the document, your app can display an alert to let them know their submission was successful.

To use ClassKit UI, add the [`ClassKit Environment Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.ClassKit-environment) entitlement in your app, which enables ClassKit integration.

## Topics

### Submitting assigned documents
- [struct AssignedDocumentSubmissionButton](assigneddocumentsubmissionbutton.md)
  A button that provides submission functionality for the assigned document.
- [class AssignedDocumentDeferredMenuElement](assigneddocumentdeferredmenuelement.md)
  A deferred menu element that provides assigned document submission functionality.
- [class AssignedDocumentMenuItem](assigneddocumentmenuitem.md)
  A menu item that provides assigned document submission functionality.
### Displaying assigned document information
- [struct AssignedDocumentLabel](assigneddocumentlabel.md)
  A view that displays the status or date information of the assigned document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ClassKitUI)*