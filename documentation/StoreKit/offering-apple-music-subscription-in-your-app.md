# Offering Apple Music Subscription in Your App

**Framework**: StoreKit

Allow eligible customers to subscribe to Apple Music.

#### Overview

With an Apple Music membership, customers can play songs from the entire Apple Music catalog or access their iCloud music library across all their devices. You can offer users the option to sign up for an Apple Music subscription directly from your app by following these steps:

1. Request Apple Music Library access from the customer.
2. Determine if the customer is eligible for an Apple Music subscription.
3. Present the sign-up subscription offer if the customer is eligible.

##### Request Apple Music Library Access

The user must grant permission before your app can access Apple Music library. See [`Requesting Access to Apple Music Library`](requesting-access-to-apple-music-library.md) for details. Use [`authorizationStatus()`](skcloudservicecontroller/authorizationstatus().md) to determine your app’s authorization status. If the authorization status is [`SKCloudServiceAuthorizationStatus.authorized`](skcloudserviceauthorizationstatus/authorized.md), your app can check if the user is eligible for an Apple Music subscription offer.

**Swift**:

```swift
SKCloudServiceController.authorizationStatus() == .authorized
```

**Objective-C**:

```objc
SKCloudServiceAuthorizationStatus status = ([SKCloudServiceController authorizationStatus] == SKCloudServiceAuthorizationStatusAuthorized); 
```

> ❗ **Important**:  When the Music app is absent on the user’s device, [`load(options:completionHandler:)`](skcloudservicesetupviewcontroller/load(options:completionhandler:).md) fails to load.

##### Determine If the User Is Eligible for an Apple Music Subscription

After getting Apple Music access from the user, call [`requestCapabilities(completionHandler:)`](skcloudservicecontroller/requestcapabilities(completionhandler:).md) on an instance of [`SKCloudServiceController`](skcloudservicecontroller.md) to query the user’s capabilities. Then, inspect the `capabilities` parameter of this method to determine eligibility. See [`Determining a person’s Apple Music capabilities`](determining-a-person-s-apple-music-capabilities.md) for details. A user has an active subscription to Apple Music when `capabilities` contains [`musicCatalogPlayback`](skcloudservicecapability/musiccatalogplayback.md). A user is eligible for the offer when `capabilities` doesn’t include [`musicCatalogPlayback`](skcloudservicecapability/musiccatalogplayback.md) but contains [`musicCatalogSubscriptionEligible`](skcloudservicecapability/musiccatalogsubscriptioneligible.md).

**Swift**:

```swift
let controller = SKCloudServiceController()
controller.requestCapabilities { (capabilities: SKCloudServiceCapability, error: Error?) in
    guard error == nil else { return }

    if capabilities.contains(.musicCatalogSubscriptionEligible) && !capabilities.contains(.musicCatalogPlayback) {
        // Allows subscription to the Apple Music catalog.
    }
}
```

**Objective-C**:

```objc
SKCloudServiceController *controller = [[SKCloudServiceController alloc] init];
    
[controller requestCapabilitiesWithCompletionHandler:^(SKCloudServiceCapability capabilities, NSError *error){
     if (error != nil) {
         // Handle error.
     } else if ((capabilities & SKCloudServiceCapabilityMusicCatalogSubscriptionEligible) && (!(capabilities & SKCloudServiceCapabilityMusicCatalogPlayback))) {
         // Allows subscription to the Apple Music catalog.
     }
}];
```

##### Present the Offer to Subscribe for Apple Music

For users who are eligible for an Apple Music subscription, use the following steps to allow users to sign up for it.

First, create a dictionary with an [`action`](skcloudservicesetupoptionskey/action.md) key to [`subscribe`](skcloudservicesetupaction/subscribe.md):

**Swift**:

```swift
let options: [SKCloudServiceSetupOptionsKey: Any] = [.action: SKCloudServiceSetupAction.subscribe]
```

**Objective-C**:

```objc
NSDictionary<SKCloudServiceSetupOptionsKey, id> *options = @{SKCloudServiceSetupOptionsActionKey: SKCloudServiceSetupActionSubscribe};
```

If you have an [`iTunes Store affiliate account`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/itcfa7936330), you can add the [`affiliateToken`](skcloudservicesetupoptionskey/affiliatetoken.md) key to the dictionary to earn commision if the user subscribes:

**Swift**:

```swift
let affiliateToken = "Your_Affiliate_Token"
let options: [SKCloudServiceSetupOptionsKey: Any] = [.action: SKCloudServiceSetupAction.subscribe, .affiliateToken: affiliateToken]
```

**Objective-C**:

```objc
NSString *affiliateToken = @"Your_Affiliate_Token";
NSDictionary<SKCloudServiceSetupOptionsKey, id> *options = @{SKCloudServiceSetupOptionsActionKey: SKCloudServiceSetupActionSubscribe, SKCloudServiceSetupOptionsAffiliateTokenKey: affiliateToken};
```

By default, the setup view is configured with the [`messageIdentifier`](skcloudservicesetupoptionskey/messageidentifier.md) key set to [`join`](skcloudservicesetupmessageidentifier/join.md). Add [`messageIdentifier`](skcloudservicesetupoptionskey/messageidentifier.md) to the dictionary and set it to [`addMusic`](skcloudservicesetupmessageidentifier/addmusic.md), [`connect`](skcloudservicesetupmessageidentifier/connect.md), or [`playMusic`](skcloudservicesetupmessageidentifier/playmusic.md) if you wish to change the default message that your app shows to the user:

**Swift**:

```swift
let options: [SKCloudServiceSetupOptionsKey: Any] = [.action: SKCloudServiceSetupAction.subscribe, .messageIdentifier: SKCloudServiceSetupMessageIdentifier.addMusic]
```

**Objective-C**:

```objc
NSDictionary<SKCloudServiceSetupOptionsKey, id> *options = @{SKCloudServiceSetupOptionsActionKey: SKCloudServiceSetupActionSubscribe, SKCloudServiceSetupOptionsMessageIdentifierKey: SKCloudServiceSetupMessageIdentifierAddMusic};
```

Next, create an [`SKCloudServiceSetupViewController`](skcloudservicesetupviewcontroller.md) object and set the view controller class as its delegate:

**Swift**:

```swift
let controller = SKCloudServiceSetupViewController()
controller.delegate = self
```

**Objective-C**:

```objc
SKCloudServiceSetupViewController *controller = [[SKCloudServiceSetupViewController alloc] init];
controller.delegate = self;
```

Then, pass the dictionary to the [`load(options:completionHandler:)`](skcloudservicesetupviewcontroller/load(options:completionhandler:).md) method of the [`SKCloudServiceSetupViewController`](skcloudservicesetupviewcontroller.md) object. Finally, present the [`SKCloudServiceSetupViewController`](skcloudservicesetupviewcontroller.md) object modally from your app:

**Swift**:

```swift
controller.load(options: options) { [weak self] (result: Bool, error: Error?) in
   guard error == nil else { return }
   
    if result {
        self?.present(controller, animated: true, completion: nil)
    }
}
```

**Objective-C**:

```objc
[controller loadWithOptions:options completionHandler:^(BOOL result, NSError *error) {
    if(error != nil) {
        // Handle error.
     } else if (result) {
        [self presentViewController:controller animated:YES completion:nil];
     }
}];
```

## See Also

- [struct SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey.md)
  Keys to specify the types of setup options for a cloud service.
- [func load(options: [SKCloudServiceSetupOptionsKey : Any], completionHandler: ((Bool, (any Error)?) -> Void)?)](skcloudservicesetupviewcontroller/load(options:completionhandler:).md)
  Loads the cloud service setup view with the specified options.
- [class SKArcadeService](skarcadeservice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/offering-apple-music-subscription-in-your-app)*