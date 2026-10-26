---
source: App-Store
framework: App-Store
url: https://developer.apple.com/app-store/app-privacy-details/
---

# App privacy details on the App Store

[Watch the latest videos about privacy](https://developer.apple.com/videos/privacy-security)

The App Store helps people better understand an app’s privacy practices before they download the app on any Apple platform. On each app’s product page, users can learn about some of the data types the app may collect, and whether that data is linked to them or used to track them. You’ll need to provide information about your app’s privacy practices, including the practices of third-party partners whose code you integrate into your app, in App Store Connect. This information is required to submit new apps and app updates to the App Store.

![](https://developer.apple.com/app-store/app-privacy-details/images/lockup-26-hero-large_2x.png)

## What’s new

An important part of submitting your app to the App Store is explaining how your app handles user data. Two new updates make it easier to accurately provide Privacy Nutrition Labels and improve the integrity of the software supply chain: signatures for third-party SDKs and privacy manifests. In addition, we’re adding more data type options to use in your Privacy Nutrition Label when describing what types of data your app collects.

- [Read more](https://developer.apple.com/news/?id=av1nevon)
- [Watch the latest videos](https://developer.apple.com/videos/privacy-security)

## Answering app privacy questions

As you get ready to select your answers from the options presented in App Store Connect, keep in mind:

- You need to identify all of the data you or your third-party partners collect, unless the data meets all of the criteria for optional disclosure listed below.
- Your app’s privacy practices should follow the App Review Guidelines and all applicable laws.
- You’re responsible for keeping your responses accurate and up to date. If your practices change, update your responses in App Store Connect. You may update your answers at any time, and you do not need to submit an app update in order to change your answers.

Account Holders, Admins, and App Managers can [learn how to enter their responses](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/) in App Store Connect.

## Data collection

The purpose of the label is to help your customers understand what data is collected from your app and how it is used. To complete that, you’ll need to know the types of data that you and/or your third-party partners collect from your app before answering the questions in App Store Connect. Keep in mind that even if you collect the data for reasons other than analytics or advertising, it still needs to be declared. For example, if you collect data solely for the purpose of app functionality, declare the data on your label and indicate that it is only being used for that purpose.

“Collect” refers to transmitting data off the device in a way that allows you and/or your third-party partners to access it for a period longer than what is necessary to service the transmitted request in real time.

“Third-party partners” refers to analytics tools, advertising networks, third-party SDKs, or other external vendors whose code you’ve added to your app.

## Optional disclosure

Data types that meet all of the following criteria are optional to disclose:

- The data is not used for tracking purposes, meaning the data is not linked with Third-Party Data for advertising or advertising measurement purposes, or shared with a data broker. For details, see the [Tracking](#user-tracking) section.
- The data is not used for Third-Party Advertising, your Advertising or Marketing purposes, or for Other Purposes, as those terms are defined in the [Tracking](#user-tracking) section.
- Collection of the data occurs only in infrequent cases that are not part of your app’s primary functionality, and which are optional for the user.
- The data is provided by the user in your app’s interface, it is clear to the user what data is collected, the user’s name or account name is prominently displayed in the submission form alongside the other data elements being submitted, and the user affirmatively chooses to provide the data for collection each time.

Data types must meet all criteria in order to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in App Store Connect.

Examples of data that may not need to be disclosed include data collected in optional feedback forms or customer service requests that are unrelated to the primary purpose of the app and meet the other criteria above.

For the purpose of clarity, data collected on an ongoing basis after an initial request for permission must be disclosed.

#### Product Improvement Programs

Data types that meet all of the following criteria are optional to disclose:

- Data collected is only used for the purpose of improving your app and its services.
- Collection of the data is optional and only occurs if the user explicitly opts in through a choice presented directly within the user interface — where the user is given two clear options: one to share the data and one to not share the data.
- The user’s choice does not impact any features or functionality of the app, or their cost.
- Users can update their choice at any time through an easily accessible setting.
- The data is not linked to the user’s identity (via their account, device, or other details).
- The data is not used for tracking purposes, meaning the data is not linked with Third-Party Data for advertising or advertising measurement purposes, or shared with a data broker. For details, see the Tracking section.
- The data is not used for Third-Party Advertising, your Advertising or Marketing purposes, Product Personalization, or Other Purposes.

Data types must meet all the criteria to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

#### Regulated Financial Services Disclosure

Data types that are collected by an app that facilitates regulated financial services and where the data collected meets all of the following criteria are optional to disclose:

- Collection of the regulated data is in accordance with a legally required privacy notice under applicable financial services or data protection laws or regulations (e.g., GDPR or GLBA).
- Collection by the app of that data occurs only in cases that are not part of your app’s primary functionality, and which are optional for the user.
- Such notice provides that data is not shared with unaffiliated third parties to market other products and services.
- Such data is not linked with third-party data for advertising purposes or shared with a data broker except for purposes of fraud detection or prevention or security purposes, or with a consumer reporting agency for credit reporting.

Data types must meet all criteria in order to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

#### Health Research Disclosure

Data types that are collected as part of a health research study and where the data collected meets all of the following criteria are optional to disclose:

- The data is collected by an entity whose collection of the data is subject to an informed consent form (ICF) as part of a health research study that has been reviewed and approved by an institutional review board or ethics review board.
- All such data collection must follow the relevant App Review Guidelines and the data may not be used for tracking purposes.

If the data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

## Types of data

Refer to the list of data types below and compare them to the data collection practices in your app.

| Contact Info |
| --- |
| Name | Such as first or last name |
| Email Address | Including but not limited to a hashed email address |
| Phone Number | Including but not limited to a hashed phone number |
| Physical Address | Such as home address, physical address, or mailing address |
| Other User Contact Info | Any other information that can be used to contact the user outside the app |
| Health & Fitness |
| Health | Health and medical data, including but not limited to data from the Clinical Health Records API, HealthKit API, Movement Disorder API, or health-related human subject research or any other user provided health or medical data |
| Fitness | Fitness and exercise data, including but not limited to the Motion and Fitness API |
| Financial Info |
| Payment Info | Such as form of payment, payment card number, or bank account number. If your app uses a payment service, the payment information is entered outside your app, and you as the developer never have access to the payment information, it is not collected and does not need to be disclosed. |
| Credit Info | Such as credit score |
| Other Financial Info | Such as salary, income, assets, debts, or any other financial information |
| Location |
| Precise Location | Information that describes the location of a user or device with the same or greater resolution as a latitude and longitude with three or more decimal places |
| Coarse Location | Information that describes the location of a user or device with lower resolution than a latitude and longitude with three or more decimal places, such as Approximate Location Services |
| Sensitive Info |
| Sensitive Info | Such as racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data |
| Contacts |
| Contacts | Such as a list of contacts in the user’s phone, address book, or social graph |
| User Content |
| Emails or Text Messages | Including subject line, sender, recipients, and contents of the email or message |
| Photos or Videos | The user’s photos or videos |
| Audio Data | The user’s voice or sound recordings |
| Gameplay Content | Such as saved games, multiplayer matching or gameplay logic, or user-generated content in-game |
| Customer Support | Data generated by the user during a customer support request |
| Other User Content | Any other user-generated content |
| Browsing History |
| Browsing History | Information about content the user has viewed that is not part of the app, such as websites |
| Search History |
| Search History | Information about searches performed in the app |
| Identifiers |
| User ID | Such as screen name, handle, account ID, assigned user ID, customer number, or other user- or account-level ID that can be used to identify a particular user or account |
| Device ID | Such as the device’s advertising identifier, or other device-level ID |
| Purchases |
| Purchase History | An account’s or individual’s purchases or purchase tendencies |
| Usage Data |
| Product Interaction | Such as app launches, taps, clicks, scrolling information, music listening data, video views, saved place in a game, video, or song, or other information about how the user interacts with the app |
| Advertising Data | Such as information about the advertisements the user has seen |
| Other Usage Data | Any other data about user activity in the app |
| Diagnostics |
| Crash Data | Such as crash logs |
| Performance Data | Such as launch time, hang rate, or energy use |
| Other Diagnostic Data | Any other data collected for the purposes of measuring technical diagnostics related to the app |
| Surroundings |
| Environment Scanning | Such as mesh, planes, scene classification, and/or image detection of the user’s surroundings |
| Body |
| Hands | The user’s hand structure and hand movements |
| Head | The user’s head movement |
| Other Data |
| Other Data Types | Any other data types not mentioned |

## Data use

You should have a clear understanding of how each data type is used by you and your third-party partners.

For example, collecting an email address and using it to authenticate the user and personalize the user’s experience within your app would include App Functionality and Product Personalization.

| Purpose | Definition |
| --- | --- |
| Third-Party Advertising | Such as displaying third-party ads in your app, or sharing data with entities who display third-party ads |
| Developer’s Advertising or Marketing | Such as displaying first-party ads in your app, sending marketing communications directly to your users, or sharing data with entities who will display your ads |
| Analytics | Using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics |
| Product Personalization | Customizing what the user sees, such as a list of recommended products, posts, or suggestions |
| App Functionality | Such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support |
| Other Purposes | Any other purposes not listed |

## Data linked to the user

You’ll need to identify whether each data type is linked to the user’s identity (via their account, device, or other details) by you and/or your third-party partners. Data collected from an app is often linked to the user’s identity, unless specific privacy protections are put in place before collection to de-identify or anonymize it, such as:

- Stripping data of any direct identifiers, such as user ID or name, before collection.
- Manipulating data to break the linkage and prevent re-linkage to real-world identities.

Additionally, in order for data not to be linked to a particular user’s identity, you must avoid certain activities after collection:

- You must not attempt to link the data back to the user’s identity.
- You must not tie the data to other datasets that enable it to be linked to a particular user’s identity.

Note: “Personal Information” and “Personal Data”, as defined under relevant privacy laws, are considered linked to the user.

## Tracking

You’ll need to understand whether you and/or your third-party partners use data from your app to track users and, if so, which data is used for this purpose.

“Tracking” refers to linking data collected from your app about a particular end-user or device, such as a user ID, device ID, or profile, with Third-Party Data for targeted advertising or advertising measurement purposes, or sharing data collected from your app about a particular end-user or device with a data broker.

“Third-Party Data” refers to any data about a particular end-user or device collected from apps, websites, or offline properties not owned by you.

Examples of tracking include:

- Displaying targeted advertisements in your app based on user data collected from apps and websites owned by other companies.
- Sharing device location data or email lists with a data broker.
- Sharing a list of emails, advertising IDs, or other IDs with a third-party advertising network that uses that information to retarget those users in other developers’ apps or to find similar users.
- Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes. For example, using a login SDK that repurposes the data it collects from your app to enable targeted advertising in other developers’ apps.

The following situations are not considered tracking:

- When the data is linked solely on the end-user’s device and is not sent off the device in a way that can identify the end-user or device.
- When the data broker uses the data shared with them solely for fraud detection or prevention or security purposes.
- When the data broker is a consumer reporting agency and the data is shared with them for purposes of (1) reporting on a consumer’s creditworthiness or (2) obtaining information on a consumer’s creditworthiness for the specific purpose of making a credit determination.

[Learn more about tracking](https://developer.apple.com/app-store/user-privacy-and-data-use/).

## Privacy links

By adding the following links on your product page, you can help users easily access your app’s privacy policy and manage their data in your app.

**Privacy Policy (Required):** The URL to your publicly accessible privacy policy.

**Privacy Choices (Optional):** A publicly accessible URL where users can learn more about their privacy choices for your app and how to manage them. For example, a webpage where users can access their data, request deletion, or make changes.

## Additional guidance

#### Your app has web views.

Data collected via web traffic must be declared, unless you are enabling the user to navigate the open web.

#### You collect and store IP address from your users.

Declare the relevant data types based on how you use IP address, such as precise location, coarse location, device ID, or diagnostics.

#### You offer in-app private messaging between users that are not SMS text messages.

Declare emails or text messages on your label. Text messages refer to both SMS and non-SMS messages.

#### Your app includes game saves, multiplayer matching, or gameplay logic.

Declare Gameplay Content on your label.

#### You collect different types of data from users depending on whether the user is a child, whether they are a free or paid user, whether they opt in, where they live, or for some other reason.

Please disclose all data collected from your app, unless it meets all of the criteria outlined in the Optional Disclosure section. You may use the Privacy Choices or Privacy Policy links to provide additional detail about how your data collection practices may vary.

#### You use Apple frameworks or services, such as MapKit, CloudKit, or App Analytics.

If you collect data about your app from Apple frameworks or services, you should indicate what data you collect and how you use it. You are not responsible for disclosing data collected by Apple.

#### You use location, device identifiers, and other sensitive data, but only on device, and the data is never sent to a server.

Data that is processed only on device is not “collected” and does not need to be disclosed in your answers. If you derive anything from that data and send it off device, the resulting data should be considered separately.

#### You collect precise location, but immediately de-identify and coarsen it before storing.

Disclose that you collect Coarse Location, since the precise location data is immediately coarsened and precise location is not stored.

#### Your app includes free-form text fields or voice recordings, and users can save any type of information they want through those mediums, including names and health data.

Mark "Other User Content" to represent generic free form text fields and "Audio Data" for voice recordings. You’re not responsible for disclosing all possible data that users may manually enter in the app through free-form fields or voice recordings. However, if you ask a user to input a specific data type into a text field, such as their name or email, or if you have a feature that enables users to upload a particular media type, such as photos or videos, then you’ll need to disclose the specific type of data.

#### You collect data to service a request but do not retain it after servicing the request.

"Collect" refers to transmitting data off the device and storing it in a readable form for longer than the time it takes you and/or your third-party partners to service the request. For example, if an authentication token or IP address is sent on a server call and not retained, or if data is sent to your servers then immediately discarded after servicing the request, you do not need to disclose this in your answers in App Store Connect.

#### You’d like your app to reference consent requests so you can comply with local privacy laws in its App Tracking Transparency prompt.

If you’ve already shown the user a required government data-privacy consent prompt that is also covered by App Tracking Transparency (for example, through a third-party Consent Management Platform), you can reference that in your app’s App Tracking Transparency purpose string. Here’s an example of a purpose string that clearly explains the user’s choice:

“[App] indicates you allowed it to use your data for advertising purposes in its legal prompt. Would you like your Apple device to provide [App] access to the advertising ID or otherwise allow it to use other means for the data processing described above?”
